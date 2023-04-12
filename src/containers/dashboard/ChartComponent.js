import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";

// Chart
import Chart from "./TodayTrendsComponent";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(1),
    textAlign: "center",
    color: theme.palette.text.secondary,
  },
}));

export default function ChartComponent() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Grid container spacing={3}>
        {/* Auto-Layout */}
        <Grid item xs>
          <Paper className={classes.paper}>
            <Chart />
          </Paper>
        </Grid>
        <Grid item xs>
          <Paper className={classes.paper}>
            <Chart />
          </Paper>
        </Grid>
      </Grid>
    </div>
  );
}

//  <Chart chartData={this.state.chartData} legendPosition="bottom" />;