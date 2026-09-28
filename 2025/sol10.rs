use std::collections::HashSet;
use std::fs;

struct Solver {
    // Pre každý joltage index množina buttonov, ktoré ho ovplyvňujú.
    joltages: Vec<HashSet<usize>>,

    // buttons[i] = indexy joltage hodnôt ovplyvnené buttonom i
    buttons: Vec<Vec<usize>>,

    best: i64,
}

impl Solver {
    fn recursive(
        &mut self,
        stats: &mut Vec<i64>,
        used_buttons: &mut HashSet<usize>,
        k: i64,
    ) {
        // Ak sme sa dostali pod nulu, táto vetva nemôže fungovať.
        if stats.iter().any(|&x| x < 0) {
            return;
        }

        // Všetky targety sme vyčerpali.
        if stats.iter().sum::<i64>() == 0 {
            self.best = self.best.min(k);
            return;
        }

        if used_buttons.len() == self.buttons.len() {
            return;
        }

        if self.best < k {
            return;
        }

        // ------------------------------------------------------------
        // Nájdeme joltage, ktorý môže ovplyvniť už iba jeden button.
        // ------------------------------------------------------------

        for jolt in 0..self.joltages.len() {
            // Python iteroval iba cez kľúče existujúce v joltages.
            if self.joltages[jolt].is_empty() {
                continue;
            }

            let remaining: Vec<usize> = self.joltages[jolt]
                .iter()
                .copied()
                .filter(|idx| !used_buttons.contains(idx))
                .collect();

            if remaining.is_empty() && stats[jolt] != 0 {
                return;
            }

            if remaining.len() == 1 {
                let chosen_idx = remaining[0];
                let count = stats[jolt];

                self.process(
                    stats,
                    used_buttons,
                    chosen_idx,
                    count,
                    k,
                );

                return;
            }
        }

        // ------------------------------------------------------------
        // Nájdeme button s minimálnym počtom možností.
        // ------------------------------------------------------------

        let mut best_mx = i64::MAX;
        let mut best_idx: Option<usize> = None;

        for idx in 0..self.buttons.len() {
            if used_buttons.contains(&idx) {
                continue;
            }

            let mut mx = i64::MAX;

            for &button_toggle in &self.buttons[idx] {
                mx = mx.min(stats[button_toggle]);
            }

            if mx < best_mx {
                best_mx = mx;
                best_idx = Some(idx);
            }
        }

        let Some(best_idx) = best_idx else {
            return;
        };

        // Vďaka kontrole stats < 0 vyššie by best_mx malo byť >= 0.
        for g in 0..=best_mx {
            self.process(
                stats,
                used_buttons,
                best_idx,
                g,
                k,
            );
        }
    }

    fn process(
        &mut self,
        stats: &mut Vec<i64>,
        used_buttons: &mut HashSet<usize>,
        button_idx: usize,
        count: i64,
        k: i64,
    ) {
        used_buttons.insert(button_idx);

        self.apply_button(stats, button_idx, -count);

        self.recursive(
            stats,
            used_buttons,
            k + count,
        );

        self.apply_button(stats, button_idx, count);

        used_buttons.remove(&button_idx);
    }

    fn apply_button(
        &self,
        stats: &mut [i64],
        button_idx: usize,
        count: i64,
    ) {
        for &v in &self.buttons[button_idx] {
            stats[v] += count;
        }
    }
}

fn solve(line: &str) -> i64 {
    let mut buttons: Vec<Vec<usize>> = Vec::new();
    let mut targets: Option<Vec<i64>> = None;

    for x in line.split_whitespace() {
        if x.starts_with('[') {
            continue;
        }

        // Ekvivalent:
        //
        // x.replace(x[0], '').replace(x[-1], '')
        //
        // Za predpokladu, že token je napr.
        // "(1,2,3)" alebo "{10,20,30}"
        let inner = &x[1..x.len() - 1];

        if x.starts_with('(') {
            let numbers: Vec<usize> = if inner.is_empty() {
                Vec::new()
            } else {
                inner
                    .split(',')
                    .map(|s| s.parse::<usize>().unwrap())
                    .collect()
            };

            buttons.push(numbers);
        } else {
            let numbers: Vec<i64> = if inner.is_empty() {
                Vec::new()
            } else {
                inner
                    .split(',')
                    .map(|s| s.parse::<i64>().unwrap())
                    .collect()
            };

            targets = Some(numbers);
        }
    }

    let targets = targets.expect("Targets not found");

    // joltages[j] obsahuje buttony, ktoré ovplyvňujú j.
    let mut joltages: Vec<HashSet<usize>> =
        vec![HashSet::new(); targets.len()];

    for (button_idx, button) in buttons.iter().enumerate() {
        for &jolt in button {
            joltages[jolt].insert(button_idx);
        }
    }

    println!("joltages = {:?}", joltages);
    println!("buttons = {:?}", buttons);

    let mut solver = Solver {
        joltages,
        buttons,
        best: i64::MAX,
    };

    let mut stats = targets;
    let mut used_buttons = HashSet::new();

    solver.recursive(
        &mut stats,
        &mut used_buttons,
        0,
    );

    solver.best
}

fn main() {
    let input = fs::read_to_string("input2510")
        .expect("Failed to read input2510");

    let mut result: i64 = 0;

    for line in input.lines() {
        result += solve(line);
        println!("{result}");
    }

    println!("{result}");
}