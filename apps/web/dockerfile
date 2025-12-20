FROM node:20-alpine AS base


FROM base AS deps

RUN apk add --no-cache libc6-compat
WORKDIR /app

COPY package.json ./
RUN npm i


FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .

RUN npm run build


FROM base AS runner
WORKDIR /app

ENV NODE_ENV=production

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nuxtjs

COPY --from=builder /app/.output ./.output

USER nuxtjs

EXPOSE 3001

ENV PORT=3001
ENV HOST="0.0.0.0"

CMD ["node", ".output/server/index.mjs"]
