import { BattingInput, BattingModel } from "./batting-model";
import { BowlingInput } from "./bowling-model"

export type PlayerInput = {
  batting_stats: BattingInput;
  bowling_stats: BowlingInput;
}

export interface PlayerModel {
  name: string;
  matches: number;
  batting_stats: BattingModel;
  bowling_stats: BowlingInput;
}