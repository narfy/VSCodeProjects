import java.awt.*;

public class Husky extends Critter {
    public Action getMove(CritterInfo info) {
        return Action.HOP;
    }

    public Color getColor() {
        return Color.BLUE;
    }

    public String toString() {
        return "H";
    }
}
