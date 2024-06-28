import { Container, TextField, Button, Typography, Box } from "@mui/material";

const GeneralForm = ({ title, fields, buttonText, onSubmit }) => {
  return (
    <Container maxWidth="sm">
      <Box
        display="flex"
        flexDirection="column"
        justifyContent="center"
        alignItems="center"
        minHeight="100vh"
      >
        <Typography variant="h4" component="h1" gutterBottom>
          {title}
        </Typography>
        <form noValidate autoComplete="off" onSubmit={onSubmit}>
          {fields.map((field, index) => (
            <TextField
              key={index}
              label={field.label}
              variant="outlined"
              type={field.type}
              margin="normal"
              fullWidth
              required={field.required}
            />
          ))}
          <Button
            variant="contained"
            color="primary"
            type="submit"
            fullWidth
            sx={{ mt: 2 }}
          >
            {buttonText}
          </Button>
        </form>
      </Box>
    </Container>
  );
};

export default GeneralForm;
