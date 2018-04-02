---
UID: NS:iscsiprf._MSiSCSI_NICPerformance
title: "_MSiSCSI_NICPerformance"
author: windows-driver-content
description: The MSiSCSI_NICPerformance structure can be used by an iSCSI initiator to report statistics for a network interface card (NIC) port.
old-location: storage\msiscsi_nicperformance.htm
old-project: storage
ms.assetid: 921e6e44-adc2-4257-b11e-941121f5bfd7
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PMSiSCSI_NICPerformance, MSiSCSI_NICPerformance, MSiSCSI_NICPerformance structure [Storage Devices], PMSiSCSI_NICPerformance, PMSiSCSI_NICPerformance structure pointer [Storage Devices], _MSiSCSI_NICPerformance, iscsiprf/MSiSCSI_NICPerformance, iscsiprf/PMSiSCSI_NICPerformance, storage.msiscsi_nicperformance, structs-iSCSI_a4d4dddd-24f6-4aa5-9b2c-61c0f1604fdb.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iscsiprf.h
req.include-header: Iscsiprf.h
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	iscsiprf.h
api_name:
-	MSiSCSI_NICPerformance
product: Windows
targetos: Windows
req.typenames: MSiSCSI_NICPerformance, *PMSiSCSI_NICPerformance
---

# _MSiSCSI_NICPerformance structure
The MSiSCSI_NICPerformance structure can be used by an iSCSI initiator to report statistics for a network interface card (NIC) port.

## Syntax
```
typedef struct _MSiSCSI_NICPerformance {
  ULONG BytesTransmitted;
  ULONG BytesReceived;
  ULONG PDUTransmitted;
  ULONG PDUReceived;
} *PMSiSCSI_NICPerformance, MSiSCSI_NICPerformance;
```

## Members


`BytesTransmitted`

The number of bytes that are transmitted through the Ethernet port.

`BytesReceived`

The number of bytes that are received through the Ethernet port.

`PDUTransmitted`

The number of PDUs that are transmitted through the Ethernet port.

`PDUReceived`

The number of PDUs that are received through the Ethernet port.

## Remarks
It is optional that you implement this class.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | iscsiprf.h (include Iscsiprf.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff563089">MSiSCSI_NICPerformance WMI Class</a>