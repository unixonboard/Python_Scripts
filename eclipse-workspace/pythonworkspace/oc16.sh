#!/bin/bash
set -e

# Manually add the host names
IPv4_HOST=$(cat /Users/thnanda/Downloads/today/ipv4_hosts.txt)
IPv6_HOST=$(cat /Users/thnanda/Downloads/today/ipv6_hosts.txt)

# Get the status after mark or unmark the hosts for removal
hostStatus(){
    fops hosts get $host | jq -r ' "id: \(.id), hostName: \(.hostName), markedForRemoval: \(.markedForRemoval)" '
    echo ""
}

markedForRemoval_IPv4()
{
    echo ""
    echo "Marking IPv4 host for removal "
    echo ""
    for host in $IPv4_HOST
    do    
        fops hosts remove --mark $host  --why "ipv6 - CHANGE-2425245"
        echo $host marked for removal
        hostStatus
    done
}


unmarkedForRemoval_IPv4()
{
    echo ""
    echo "Un-Marking IPv4 host for removal"
    echo ""
    for host in $IPv4_HOST
    do    
        fops hosts remove --no-mark $host  --why " unmarking after ipv6 - CHANGE-2425245"
        echo $host unmarked for removal
        hostStatus
    done
}


markedForRemoval_IPv6()
{
    echo ""
    echo "Marking IPv6 host for removal"
    echo ""
    for host in $IPv6_HOST
    do    
        fops hosts remove --mark $host  --why "ipv6 DoNotUse CHANGE-2425245"
        echo $host marked for removal
        hostStatus
    done
}


unmarkedForRemoval_IPv6()
{
    echo ""
    echo "Un-Marking IPv6 host for removal"
    echo ""
    for host in $IPv6_HOST
    do    
        fops hosts remove --no-mark $host  --why "ipv6 - CHANGE-2425245"
        echo $host unmarked for removal
        hostStatus
    done
}


echo "Please pass the option from below with command:
1. markedForRemoval_IPv4
2. unmarkedForRemoval_IPv4
3. markedForRemoval_IPv6
4. unmarkedForRemoval_IPv6
"

read -p "Enter an Option: " opt \n

case $opt
in
    1) markedForRemoval_IPv4 ;;
    2) unmarkedForRemoval_IPv4 ;;
    3) markedForRemoval_IPv6 ;;
    4) unmarkedForRemoval_IPv6 ;;
    *) echo "Nothing to do"
    exit ;;
esac   
