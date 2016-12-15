Usage:
-----
``` python check_rns.py <schema_src> <schema_diff> ```

Example:
-------
```
➜  rn_check git:(master) ✗ ./check_rns.py elcap_mr6-UCSM-OUT.xsd
Granada-UCSM-OUT.xsd                          
Mo: storageLocalDiskPartition Prev:partition New:partition-[id]
Mo: firmwareUcscInfo Prev:ucsc-info New:fw-ucsc-info
Mo: initiatorFcInitiatorEp Prev:fc-ini-[name] New:fc-ini-[wwpn]
Mo: licenseTarget Prev:slot-[slotId]port-[portId]
New:slot-[slotId]-aggr-port-[aggrPortId]-port-[portId]
Mo: initiatorIScsiInitiatorEp Prev:scsi-ini-[name] New:scsi-ini-[iqn]
➜  rn_check git:(master) ✗

```
