---
UID : NS:hbaapi.HBA_ipaddress
title : HBA_ipaddress
author : windows-driver-content
description : The HBA_ipaddress structure specifies an IP address in a way that is independent of the version of the IP protocol in use.
old-location : storage\hba_ipaddress.htm
old-project : storage
ms.assetid : c3f79350-29e8-4e31-a31d-359c9781777d
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : storage.hba_ipaddress, hbaapi/HBA_ipaddress, HBA_IPADDRESS, PHBA_IPADDRESS, HBA_ipaddress, HBA_ipaddress structure [Storage Devices], HBA_IPADDRESS structure [Storage Devices], structs-Fibre_8ac1972d-ec33-4642-8dfe-3d913913ca66.xml, hbaapi/PHBA_IPADDRESS, *PHBA_IPADDRESS, PHBA_IPADDRESS structure pointer [Storage Devices]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : hbaapi.h
req.include-header : Hbaapi.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PHBA_IPADDRESS, HBA_IPADDRESS"
---

# HBA_ipaddress structure
The HBA_ipaddress structure specifies an IP address in a way that is independent of the version of the IP protocol in use.

## Syntax
````
typedef struct HBA_ipaddress {
  int   ipversion;
  union {
    unsigned char ipv4address[4];
    unsigned char ipv6address[16];
  } ipaddress;
} HBA_IPADDRESS, *PHBA_IPADDRESS;
````

## Members


`ipaddress`



`ipversion`

Indicates the version of the IP protocol in use.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | hbaapi.h (include Hbaapi.h) |