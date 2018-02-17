---
UID: NS:hbaapi.HBA_ipaddress
title: HBA_ipaddress
author: windows-driver-content
description: The HBA_ipaddress structure specifies an IP address in a way that is independent of the version of the IP protocol in use.
old-location: storage\hba_ipaddress.htm
old-project: storage
ms.assetid: c3f79350-29e8-4e31-a31d-359c9781777d
ms.author: windowsdriverdev
ms.date: 1/10/2018
ms.keywords: PHBA_IPADDRESS, HBA_ipaddress, *PHBA_IPADDRESS, storage.hba_ipaddress, hbaapi/PHBA_IPADDRESS, structs-Fibre_8ac1972d-ec33-4642-8dfe-3d913913ca66.xml, PHBA_IPADDRESS structure pointer [Storage Devices], hbaapi/HBA_ipaddress, HBA_IPADDRESS, HBA_ipaddress structure [Storage Devices], HBA_IPADDRESS structure [Storage Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hbaapi.h
req.include-header: Hbaapi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	hbaapi.h
apiname:
-	HBA_IPADDRESS
product: Windows
targetos: Windows
req.typenames: HBA_IPADDRESS, *PHBA_IPADDRESS
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
| **Header** | hbaapi.h (include Hbaapi.h) |