package view

import java.awt.Button

import javafx.scene.Scene
import javafx.scene.layout.VBox
import scalafx.application.JFXApp
import scalafx.application.JFXApp.PrimaryStage
import scalafx.scene.control.TextField

object TriviaGameGUI extends JFXApp{
  val inputDisplay: TextField = new TextField{
    style = "-fx-font: 18 ariel;"
  }
  val outputDisplay: TextField = new TextField{
    style = "-fx-font: 18 ariel;"
  }
  val button: Button = new Button {
  }
  this.stage = new PrimaryStage {
    title = "GUI Example"
    scene = new Scene() {
      content = List(
        new VBox() {
          children = List(inputDisplay, button, outputDisplay)
        }
      )
    }
  }
}
