type OversModel = {
  complete_overs: number;
  partial_overs: number;
}

type BestBowlingModel = {
  wickets: number;
  runs_conceded: number;
  enabled: boolean;
}

export type BowlingInput = {
  overs: OversModel;
  runs_conceded: number;
  wickets: number;
}

export interface BowlingModel {
  overs: OversModel;
  runs_conceded: number;
  wickets: number;
  bowling_average: number;
  economy_rate: number;
  best_bowling: BestBowlingModel;
  purple_cap: number;
}