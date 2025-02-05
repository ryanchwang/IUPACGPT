class RNNDecoder(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNNDecoder, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x, hidden):
        x, hidden = self.lstm(x, hidden)
        return self.fc(x), hidden
