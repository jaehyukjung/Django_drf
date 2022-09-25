import { useMatch } from "react-router-dom";
import styled from "styled-components";

const Container = styled.section`
    display: flex;
    width: 90%;
    position: relative;
`

const Step = styled.div`
    display : flex ;
    position: absolute;
    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
    border-radius: 15px;
`

const StepArrow = styled.div`
    position: absolute;
    left: 166px; // 길이 StepBox의 width에 맞춰서
    border-top: 60px solid transparent;
    border-top-left-radius: 15px;
    border-bottom-left-radius: 15px;
    border-left: ${(props) => props.isActive ? "20px solid rgb(255,234,122)" : "20px solid #D9D9D9"};
    border-bottom: 60px solid transparent;
`

const StepBox = styled.div`
    background-color: ${(props) => props.isActive ? "rgb(255,234,122)" : "#D9D9D9"};
    width: 170px;
    border-radius : 15px;
    height: 120px;

    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    padding-left: 20px;
    padding-bottom: 30px;
`
const Num = styled.span`
    font-size: 18px;
`

const Title = styled.h6`
    font-size: 28px;
    font-weight: 700;
`

const LastStepBox = styled.div`
    background-color: #D9D9D9;
    width: 200px;
    border-radius : 15px;
    height: 120px;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    padding-left: 80px;
    padding-bottom: 30px;
`


function Nav() {
    const howMatch = useMatch("/how");
    const soundMatch = useMatch("/sound/*");

    return(
        <Container>
            <Step style={{zIndex : 4}}>
                <StepBox isActive={howMatch !== null}>
                    <Num>1단계</Num>
                    <Title>주문방법</Title>
                </StepBox>
                <StepArrow isActive={howMatch !== null}></StepArrow>
            </Step>
            <Step style={{zIndex:3, left: "145px"}}>
                <StepBox isActive={soundMatch !== null} style={{paddingLeft: "50px"}}>
                    <Num>2단계</Num>
                    <Title>메뉴선택</Title>
                </StepBox>
                <StepArrow isActive={soundMatch !== null}></StepArrow>
            </Step>
            <Step style={{zIndex:2, left: "290px"}}>
                <StepBox style={{paddingLeft: "50px"}}>
                    <Num>3단계</Num>
                    <Title>결제&정립</Title>
                </StepBox>
                <StepArrow></StepArrow>
            </Step>
            <Step style={{zIndex : 1, left: "420px"}}>
                <LastStepBox>
                    <Num>4단계</Num>
                    <Title>주문완료</Title>
                </LastStepBox>
            </Step>
            
        </Container>
    );
}

export default Nav;