FROM alpine:3.20

RUN apk add --no-cache \
    cups \
    cups-client \
    avahi \
    avahi-tools \
    dbus

# Configure CUPS for remote access, IPP, and Web UI
RUN sed -i \
      -e 's/^Listen localhost:631/Port 631/' \
      -e 's/^Listen 127\.0\.0\.1:631/Port 631/' \
      -e 's/^WebInterface No/WebInterface Yes/' \
      -e 's/^Browsing Off/Browsing On/' \
      -e 's/^DefaultEncryption Required/DefaultEncryption Never/' \
      -e 's/Allow @LOCAL/Allow all/g' \
      -e '/<Location \/>/,/<\/Location>/ s/Order allow,deny/Order allow,deny\n  Allow all/' \
      -e '/<Location \/admin>/,/<\/Location>/ s/Order allow,deny/Order allow,deny\n  Allow all\n  Encryption Never/' \
      -e '/<Location \/admin>/,/<\/Location>/ s/^  AuthType Default/  AuthType None/' \
      -e '/<Location \/admin>/,/<\/Location>/ s/^  Require user @SYSTEM/#  Require user @SYSTEM/' \
      -e '/<Location \/admin\/conf>/,/<\/Location>/ s/Order allow,deny/Order allow,deny\n  Allow all\n  Encryption Never/' \
      -e '/<Location \/admin\/conf>/,/<\/Location>/ s/^  AuthType Default/  AuthType None/' \
      -e '/<Location \/admin\/conf>/,/<\/Location>/ s/^  Require user @SYSTEM/#  Require user @SYSTEM/' \
      -e '/<Location \/admin\/log>/,/<\/Location>/ s/Order allow,deny/Order allow,deny\n  Allow all\n  Encryption Never/' \
      -e '/<Location \/admin\/log>/,/<\/Location>/ s/^  AuthType Default/  AuthType None/' \
      -e '/<Location \/admin\/log>/,/<\/Location>/ s/^  Require user @SYSTEM/#  Require user @SYSTEM/' \
      -e '/<Limit CUPS-Add-Modify-Printer/,/<\/Limit>/ s/^    AuthType Default/    AuthType None/' \
      -e '/<Limit CUPS-Add-Modify-Printer/,/<\/Limit>/ s/^    Require user @SYSTEM/#    Require user @SYSTEM/' \
      -e '/<Limit CUPS-Add-Modify-Printer/,/<\/Limit>/ s/^    Order deny,allow/    Order deny,allow\n    Allow all/' \
      -e '/<Limit Pause-Printer/,/<\/Limit>/ s/^    AuthType Default/    AuthType None/' \
      -e '/<Limit Pause-Printer/,/<\/Limit>/ s/^    Require user @SYSTEM/#    Require user @SYSTEM/' \
      -e '/<Limit Pause-Printer/,/<\/Limit>/ s/^    Order deny,allow/    Order deny,allow\n    Allow all/' \
      /etc/cups/cupsd.conf \
  && printf '\nServerAlias *\nDefaultAuthType Basic\nDefaultEncryption Never\nBrowseLocalProtocols dnssd\n' >> /etc/cups/cupsd.conf

# Basic Avahi config (mDNS/Bonjour)
RUN sed -i \
      -e 's/^#enable-dbus=yes/enable-dbus=yes/' \
      -e 's/^#publish-workstation=yes/publish-workstation=no/' \
      /etc/avahi/avahi-daemon.conf

EXPOSE 631 5353/udp

CMD ["/bin/sh", "-c", "set -e; mkdir -p /run/dbus /run/avahi-daemon; rm -f /run/dbus/pid /run/dbus/system_bus_socket /run/avahi-daemon/pid; dbus-uuidgen --ensure=/etc/machine-id; dbus-daemon --system --nofork --nopidfile & sleep 1; avahi-daemon --daemonize --no-chroot; exec cupsd -f"]
