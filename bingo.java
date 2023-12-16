import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

public class BingoGame extends JFrame {
    private int[][] card = new int[5][5];
    private JButton[][] buttons = new JButton[5][5];
    private JPanel bingoPanel;

    public BingoGame() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(300, 300);
        setTitle("ビンゴゲーム");

        bingoPanel = new JPanel(new GridLayout(5, 5));
        generateCard();

        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                JButton button = new JButton(card[i][j] == 0 ? "" : String.valueOf(card[i][j]));
                button.addActionListener(new ActionListener() {
                    @Override
                    public void actionPerformed(ActionEvent e) {
                        JButton clickedButton = (JButton) e.getSource();
                        clickedButton.setEnabled(false);
                        // ここでビンゴの判定を行うロジックを呼び出す
                    }
                });
                buttons[i][j] = button;
                bingoPanel.add(button);
            }
        }

        add(bingoPanel);
        setVisible(true);
    }

    private void generateCard() {
        Random rand = new Random();
        for (int i = 0; i < 5; i++) {
            int start = 1 + i * 20; // 各列の開始値
            for (int j = 0; j < 5; j++) {
                if (i == 2 && j == 2) {
                    card[i][j] = 0; // 真ん中の空きマス
                } else {
                    card[i][j] = rand.nextInt(19) + start;
                }
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new BingoGame();
            }
        });
    }
}