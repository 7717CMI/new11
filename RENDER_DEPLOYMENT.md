# Render Deployment Guide

This guide will help you deploy the Customer Intelligence Dashboard to Render using Docker.

## Prerequisites

- A [Render](https://render.com) account (free tier available)
- Git repository with your code (GitHub, GitLab, or Bitbucket)

## Deployment Steps

### 1. Push Your Code to Git

Make sure all your code is committed and pushed to a Git repository:

```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

### 2. Create a New Web Service on Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** and select **"Web Service"**
3. Connect your Git repository
4. Select your repository from the list

### 3. Configure Your Web Service

Fill in the following settings:

**Basic Settings:**
- **Name:** `customer-intelligence-dashboard` (or your preferred name)
- **Environment:** `Docker`
- **Region:** Choose the region closest to you
- **Branch:** `main` (or your default branch)

**Build & Deploy:**
- **Dockerfile Path:** `./Dockerfile` (default)
- **Docker Command:** (leave empty, CMD in Dockerfile will be used)

**Instance Type:**
- **Free** (for testing) or **Starter** (for production)

### 4. Environment Variables

Add the following environment variables in the Render dashboard:

| Key | Value | Description |
|-----|-------|-------------|
| `PORT` | `8050` | Port for the application (Render will override this automatically) |
| `HOST` | `0.0.0.0` | Host binding (allows external connections) |
| `DASH_DEBUG` | `False` | Disable debug mode in production |

**Note:** Render automatically sets the `PORT` environment variable, so the app will use Render's assigned port.

### 5. Advanced Settings (Optional)

**Health Check Path:** `/`
- This allows Render to verify your app is running correctly

**Auto-Deploy:** Enable
- Automatically deploy when you push to your main branch

### 6. Deploy

Click **"Create Web Service"** and Render will:
1. Clone your repository
2. Build the Docker image
3. Deploy your application
4. Assign you a public URL (e.g., `https://your-app.onrender.com`)

### 7. Monitor Deployment

Watch the deployment logs in real-time:
- Build logs will show Docker image creation
- Deploy logs will show the application starting
- Look for: `"Dash is running on http://0.0.0.0:PORT/"`

## Post-Deployment

### Access Your Dashboard

Once deployed, your dashboard will be available at:
```
https://your-app-name.onrender.com
```

### Verify Functionality

1. Check that all pages load correctly:
   - Overview Dashboard
   - Customer Details
   - Analytics Deep-Dive

2. Test filters on the Overview and Analytics pages

3. Verify data tables work correctly

## Troubleshooting

### Common Issues

**1. Application fails to start**
- Check deployment logs for errors
- Verify all environment variables are set correctly
- Ensure `requirements.txt` includes all dependencies

**2. Port binding errors**
- Make sure `HOST=0.0.0.0` is set
- Verify the app uses `os.getenv('PORT')` to get the port

**3. Application runs but shows errors**
- Check the application logs in Render dashboard
- Verify sample data is being generated correctly
- Check for any missing Python packages

**4. Slow initial load**
- Free tier instances spin down after inactivity
- First request may take 30-60 seconds to wake up
- Consider upgrading to a paid tier for always-on instances

### Viewing Logs

1. Go to your web service in Render dashboard
2. Click on **"Logs"** tab
3. View real-time application logs

### Manual Deploy

If auto-deploy is disabled, you can manually deploy:
1. Go to your web service
2. Click **"Manual Deploy"**
3. Select **"Deploy latest commit"**

## Updating Your Deployment

1. Make changes to your code locally
2. Commit and push to your Git repository:
   ```bash
   git add .
   git commit -m "Update dashboard"
   git push origin main
   ```
3. Render will automatically rebuild and deploy (if auto-deploy is enabled)

## Cost Optimization

**Free Tier:**
- Suitable for testing and personal projects
- Spins down after 15 minutes of inactivity
- 750 hours/month free

**Starter Tier ($7/month):**
- Always-on instance
- Better performance
- No spin-down delays

## Security Recommendations

1. **Environment Variables:** Store sensitive data in environment variables, not in code
2. **HTTPS:** Render provides free SSL certificates automatically
3. **Authentication:** Consider adding authentication for production use
4. **Rate Limiting:** Implement rate limiting for production deployments

## Performance Optimization

1. **Worker Configuration:** The Dockerfile uses 4 workers and 2 threads
   - Adjust based on your instance size
   - Free tier: Use 2 workers
   - Starter tier: Use 4 workers

2. **Caching:** Consider implementing caching for frequently accessed data

3. **Database:** For production, consider using a persistent database instead of CSV files

## Additional Resources

- [Render Documentation](https://render.com/docs)
- [Render Docker Deployment](https://render.com/docs/docker)
- [Dash Deployment Guide](https://dash.plotly.com/deployment)

## Support

If you encounter issues:
1. Check Render's status page: https://status.render.com/
2. Review Render documentation: https://render.com/docs
3. Contact Render support through their dashboard

---

**Deployment Checklist:**
- [ ] Code pushed to Git repository
- [ ] Dockerfile created and tested
- [ ] requirements.txt updated with all dependencies
- [ ] Environment variables configured in Render
- [ ] Web service created on Render
- [ ] Deployment successful
- [ ] Application accessible via public URL
- [ ] All features tested and working
