import { useNavigate } from "react-router-dom";
import styled from "styled-components";
import img from "../mainC.png"

const Background = styled.div`
    width: 100vw;
    height: 100vh;
    background-color: ${props => props.theme.BackColor};
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
`

const Img = styled.img`
    width: ${props => props.theme.bwh};
    height: ${props => props.theme.bwh};
`
const Title = styled.h1`
    color : ${props => props.theme.White};
    font-size:  ${props => props.theme.font};
    font-weight: 700;
    margin-top: 40px;
    margin-bottom: 20px;
`
const SubTitle = styled.h3`
    color : ${props => props.theme.White};
    font-size: 20px;
    margin-bottom: 20px;
`
const Btn = styled.button`
    margin-bottom: 50px;
    border: none;
    width : 200px;
    height: 100px;
    border-radius: 20px;
    box-shadow: rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px;
    cursor: pointer;
    p{
        font-size: 30px;
        font-weight: 700;
    }
    &:active{
        box-shadow: none;
        background-color: ${props=>props.theme.Yellow};
    }
`

function Start () {
    const navigate = useNavigate();
    const onClick = () => {
        navigate("/how");
    }

    return(
        <Background>
            <Img src={img} />
            <Title>
            어서오세요
            </Title>
            <SubTitle>
                주문하시려면 아래 시작하기 버튼을 눌러주세요.
            </SubTitle>
            <Btn onClick={onClick} >
                <p>시작하기</p>
            </Btn>
        </Background>
    )
}

export default Start;