export type BattingInput = {
  runs: number;
  balls_faced: number;
  fours: number;
  sixes: number;
}

export interface BattingModel {
  innings: number;
  runs: number;
  balls_faced: number;
  strike_rate: number;
  fours: number;
  sixes: number;
  average_runs: number;
  highest_score: number;
  fifty: number;
  century: number;
  orange_cap: number;
}
