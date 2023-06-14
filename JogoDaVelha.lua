-- Função para desenhar o tabuleiro
function desenharTabuleiro(tabuleiro)
    for i = 1, 3 do
        local linha = ""
        for j = 1, 3 do
            linha = linha .. " " .. tabuleiro[i][j] .. " "
            if j ~= 3 then
                linha = linha .. "|"
            end
        end
        print(linha)
        if i ~= 3 then
            print("---+---+---")
        end
    end
end

-- Função para verificar se há um vencedor
function verificarVencedor(tabuleiro)
    -- Verificar linhas
    for i = 1, 3 do
        if tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][1] == tabuleiro[i][3] then
            return tabuleiro[i][1]
        end
    end

    -- Verificar colunas
    for j = 1, 3 do
        if tabuleiro[1][j] == tabuleiro[2][j] and tabuleiro[1][j] == tabuleiro[3][j] then
            return tabuleiro[1][j]
        end
    end

    -- Verificar diagonais
    if tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[1][1] == tabuleiro[3][3] then
        return tabuleiro[1][1]
    end
    if tabuleiro[1][3] == tabuleiro[2][2] and tabuleiro[1][3] == tabuleiro[3][1] then
        return tabuleiro[1][3]
    end

    return nil
end

-- Função para verificar se o tabuleiro está cheio
function verificarEmpate(tabuleiro)
    for i = 1, 3 do
        for j = 1, 3 do
            if tabuleiro[i][j] == " " then
                return false
            end
        end
    end
    return true
end

-- Função principal
function jogarJogoDaVelha()
    -- Criar tabuleiro vazio
    local tabuleiro = {
        {" ", " ", " "},
        {" ", " ", " "},
        {" ", " ", " "}
    }

    -- Variável para controlar o jogador atual
    local jogadorAtual = "X"

    -- Loop principal do jogo
    while true do
        -- Desenhar o tabuleiro
        desenharTabuleiro(tabuleiro)

        -- Solicitar a jogada do jogador
        print("É a vez do jogador " .. jogadorAtual .. ". Digite a linha (1-3): ")
        local linha = tonumber(io.read())
        print("Digite a coluna (1-3): ")
        local coluna = tonumber(io.read())

        -- Validar jogada e atualizar o tabuleiro
        if linha >= 1 and linha <= 3 and coluna >= 1 and coluna <= 3 and tabuleiro[linha][coluna] == " " then
            tabuleiro[linha][coluna] = jogadorAtual

            -- Verificar se há um vencedor
            local vencedor = verificarVencedor(tabuleiro)
            if vencedor then
                desenhar
