class ImgToSMILES(nn.Module):
    def __init__(self, vocab_size):
        super(ImageToSMILES, self).__init__()
        self.encoder = CNNEncoder()
        self.decoder = RNNDecoder(256, 512, vocab_size)

    def forward(self, image, captions):
        features = self.encoder(image).unsqueeze(1)
        outputs, _ = self.decoder(features, None)
        return outputs
