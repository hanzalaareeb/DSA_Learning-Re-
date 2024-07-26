document.addEventListener("DOMContentLoaded", function () {
  createSinglyLinkedList();
  createDoublyLinkedList();
});

function createSinglyLinkedList() {
  const singlyNodes = document.getElementById("singly-nodes");
  singlyNodes.innerHTML = "";
  for (let i = 1; i <= 5; i++) {
    const node = document.createElement("div");
    node.className = "node";
    node.innerHTML = `<div>${i}</div>`;
    singlyNodes.appendChild(node);
  }
}

function createDoublyLinkedList() {
  const doublyNodes = document.getElementById("doubly-nodes");
  doublyNodes.innerHTML = "";
  for (let i = 1; i <= 5; i++) {
    const node = document.createElement("div");
    node.className = "node doubly-node";
    node.innerHTML = `<div>${i}</div>`;
    doublyNodes.appendChild(node);
  }
}

function reverseSinglyLinkedList() {
  const explanation = document.getElementById("explanation");
  explanation.innerHTML = "Reversing Singly Linked List:";

  const nodes = document.querySelectorAll("#singly-nodes .node");
  let prev = null;
  let current = 0;

  function reverseStep() {
    if (current < nodes.length) {
      if (prev !== null) {
        nodes[prev].querySelector("div").style.backgroundColor = "grey";
      }
      nodes[current].querySelector("div").style.backgroundColor = "red";
      explanation.innerHTML += `<br>Reversing link for node ${
        nodes[current].querySelector("div").textContent
      }`;

      setTimeout(() => {
        prev = current;
        current++;
        reverseStep();
      }, 1000);
    } else {
      explanation.innerHTML += "<br>Reversal complete!";
      for (let i = nodes.length - 1; i >= 0; i--) {
        document.getElementById("singly-nodes").appendChild(nodes[i]);
        nodes[i].style.transform = `translateX(${
          (nodes.length - 1 - i) * 100
        }px)`;
      }
      nodes.forEach(
        (node) => (node.querySelector("div").style.backgroundColor = "#007bff")
      );
    }
  }

  reverseStep();
}

function reverseDoublyLinkedList() {
  const explanation = document.getElementById("explanation");
  explanation.innerHTML = "Reversing Doubly Linked List:";

  const nodes = document.querySelectorAll("#doubly-nodes .node");
  let prev = null;
  let current = 0;

  function reverseStep() {
    if (current < nodes.length) {
      if (prev !== null) {
        nodes[prev].querySelector("div").style.backgroundColor = "grey";
      }
      nodes[current].querySelector("div").style.backgroundColor = "red";
      explanation.innerHTML += `<br>Reversing links for node ${
        nodes[current].querySelector("div").textContent
      }`;

      setTimeout(() => {
        prev = current;
        current++;
        reverseStep();
      }, 1000);
    } else {
      explanation.innerHTML += "<br>Reversal complete!";
      for (let i = nodes.length - 1; i >= 0; i--) {
        document.getElementById("doubly-nodes").appendChild(nodes[i]);
        nodes[i].style.transform = `translateX(${
          (nodes.length - 1 - i) * 100
        }px)`;
      }
      nodes.forEach(
        (node) => (node.querySelector("div").style.backgroundColor = "#007bff")
      );
    }
  }

  reverseStep();
}
