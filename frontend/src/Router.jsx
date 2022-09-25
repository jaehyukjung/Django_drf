import { BrowserRouter, Route, Routes } from "react-router-dom";
import Start from "./routes/Start";
import How from './routes/How';
import Touch from './routes/Touch';
import Sound from "./routes/Sound";

function Router() {
    return (
    <BrowserRouter>
        <Routes>
            {/* 시작 페이지 */}
            <Route path="/" element={<Start />}/>

            {/* 주문 방식 선택 페이지 */}
            <Route path="/how" element={<How />}/>

            {/* 터치방식 주문 페이지 */}
            <Route path="/touch" element={<Touch />}>

            </Route>

            {/* 음성 주문 페이지 */}
            <Route path = "/sound" element={<Sound />}>
                
            </Route>

        </Routes>
    </BrowserRouter>
    );
}

export default Router;