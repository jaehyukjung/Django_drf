import styled from "styled-components";

const Background = styled.div`
    width: 100vw;
    height: 100vh;
    background-color: ${props => props.theme.BackColor};
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
`

function Touch() {
    return(
        <Background>
            터치결제
        </Background>
    )
}

export default Touch;