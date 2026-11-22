# Reproduce the course-authored companion to the instructor-supplied dice chart.
# All eight sequences are theoretical outcomes of three independent fair tosses.
out <- 'assets/inferential-statistics/binomial-three-toss-arrangements.svg'
svg(out, width=7.2, height=3.05, pointsize=15, bg='white')
par(mar=c(3.5,4.2,2.1,1),mgp=c(2.4,.6,0),tcl=-.25,family='sans')
plot(NA, xlim=c(-.55,3.55), ylim=c(0,.45), xaxs='i',yaxs='i',
     xaxt='n',yaxt='n', xlab='Number of heads, X',ylab='Probability',bty='l')
axis(1,at=0:3)
axis(2,at=(0:3)/8,labels=c('0','1/8','2/8','3/8'),las=1)
groups <- list('TTT',c('HTT','THT','TTH'),c('HHT','HTH','THH'),'HHH')
for (k in 0:3) {
  sequences <- groups[[k+1]]
  for (j in seq_along(sequences)) {
    rect(k-.36,(j-1)/8,k+.36,j/8,
         col=if(k==2)'#EEE7EA' else '#EEEEEE',
         border=if(k==2)'#763D52' else '#777777',lwd=1.5)
    text(k,(j-.5)/8,sequences[j],cex=.95,
         col=if(k==2)'#542638' else '#303030',font=2)
  }
  text(k,length(sequences)/8+.035,
       if(length(sequences)==1)'1 sequence' else '3 sequences',cex=.76)
}
mtext('Each sequence has probability 1/8; each column adds its sequences.',side=3,line=.35,cex=.83)
dev.off()
stopifnot(identical(lengths(groups),c(1L,3L,3L,1L)), choose(3,2)==3,
          choose(10,2)==45, abs(dbinom(2,3,.5)-3/8)<1e-12)
