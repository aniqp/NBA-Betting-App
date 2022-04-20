function deleteBet(betID) {
    fetch("/delete-bet", {
        method: "POST",
        body: JSON.stringify({betID: betID})
    }).then((_res) => {
        window.location.href="/my-bets";
    });
}

function checkBetStatus(betID) {
    // fetch("/check-bet-status", {
    //     method: "POST",
    //     body: JSON.stringify({betID: betID})
    // }).then((_res) => {
    //     window.location.href="/my-bets";
    // });
}