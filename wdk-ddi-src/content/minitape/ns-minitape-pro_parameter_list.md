---
UID: NS:minitape.PRO_PARAMETER_LIST
title: PRO_PARAMETER_LIST
author: windows-driver-content
description: The PRO_PARAMETER_LIST structure is sent in a Persistent Reserve Out command to a device server.
old-location: storage\pro_parameter_list.htm
old-project: storage
ms.assetid: 96c128e1-c38a-412f-adeb-cde820e1af4e
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PPRO_PARAMETER_LIST, PPRO_PARAMETER_LIST, PPRO_PARAMETER_LIST structure pointer [Storage Devices], PRO_PARAMETER_LIST, PRO_PARAMETER_LIST structure [Storage Devices], storage.pro_parameter_list, storport/PPRO_PARAMETER_LIST, storport/PRO_PARAMETER_LIST, structs-general_7481edb0-cc60-44b9-abcc-80bf0f79fbae.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: minitape.h
req.include-header: Ntddstor.h, Minitape.h, Scsi.h
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
-	storport.h
api_name:
-	PRO_PARAMETER_LIST
product: Windows
targetos: Windows
req.typenames: PRO_PARAMETER_LIST, *PPRO_PARAMETER_LIST
---

# PRO_PARAMETER_LIST structure
The PRO_PARAMETER_LIST structure is sent in a Persistent Reserve Out command to a device server.

## Syntax
```
typedef struct PRO_PARAMETER_LIST {
  UCHAR      ReservationKey[8];
  UCHAR      ServiceActionReservationKey[8];
  UCHAR      ScopeSpecificAddress[4];
  UCHAR  : 1 ActivatePersistThroughPowerLoss;
  UCHAR  : 7 Reserved1;
  UCHAR      Reserved2;
  UCHAR      Obsolete[2];
} *PPRO_PARAMETER_LIST, PRO_PARAMETER_LIST;
```

## Members


`ReservationKey`

The ReservationKey field contains an 8-byte value that is provided by the application client to the device server. This value identifies the initiator that is the source of the Persistent Reserve Out command.

`ServiceActionReservationKey`

The ServiceActionReservationKey field contains information that is needed for the following four service actions:

<ul>
<li>
REGISTER

</li>
<li>
REGISTER AND IGNORE EXISTING KEY

</li>
<li>
PREEMPT

</li>
<li>
PREEMPT AND ABORT

</li>
</ul>

`ScopeSpecificAddress`

The ScopeSpecificAddress field contains the element address that has zeros placed in the most significant bits to fit the field. This is true if the scope of a reservation is set to ELEMENT_SCOPE. Otherwise, this field is set to all zeros.

`ActivatePersistThroughPowerLoss`

The ActivatePersistThroughPowerLoss (APTPL) bit is valid only for the following service actions:

<ul>
<li>
REGISTER

</li>
<li>
REGISTER AND IGNORE EXISTING KEY

</li>
</ul>

`Reserved1`

Reserved. Must be zero.

`Reserved2`

Reserved. Must be zero.

`Obsolete`

Reserved. Must be zero.

## Remarks
The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560586">IOCTL_STORAGE_PERSISTENT_RESERVE_OUT</a> request is used to control information about persistent reservations and reservation keys that are active within a device server.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | minitape.h (include Ntddstor.h, Minitape.h, Scsi.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560586">IOCTL_STORAGE_PERSISTENT_RESERVE_OUT</a>