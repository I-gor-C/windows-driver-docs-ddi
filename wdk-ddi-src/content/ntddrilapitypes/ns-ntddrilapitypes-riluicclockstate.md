---
UID: NS:ntddrilapitypes.RILUICCLOCKSTATE
title: RILUICCLOCKSTATE
author: windows-driver-content
description: This structure represents a RILUICCLOCKSTATE.
old-location: netvista\riluicclockstate.htm
old-project: netvista
ms.assetid: bc27f7b8-8de0-4eae-a22b-0e5c76378b1a
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: "*LPRILUICCLOCKSTATE, RILUICCLOCKSTATE, RILUICCLOCKSTATE structure [Network Drivers Starting with Windows Vista], netvista.riluicclockstate, rilapitypes/RILUICCLOCKSTATE"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddrilapitypes.h
req.include-header: Ntddrilapitypes.h
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
-	rilapitypes.h
api_name:
-	RILUICCLOCKSTATE
product: Windows
targetos: Windows
req.typenames: RILUICCLOCKSTATE, *LPRILUICCLOCKSTATE
---

# RILUICCLOCKSTATE structure
<div class="alert"><b>Warning</b>  The Cellular COM API is deprecated in Windows 10. This content is provided to support maintenance of OEM and mobile operator created Windows Phone 8.1 applications.</div><div> </div>This structure represents a RILUICCLOCKSTATE.

## Syntax
````
struct RILUICCLOCKSTATE {
  DWORD       cbSize;
  DWORD       dwParams;
  RILUICCLOCK rilUiccLock;
  DWORD       dwLockState;
  DWORD       dwVerifyAttemptsLeft;
  DWORD       dwUnblockAttemptsLeft;
};
````

## Members


`cbSize`

The size of the structure in bytes.

`dwParams`

A bitwise combination of <a href="..\rilapitypes\ne-rilapitypes-riluicclockstateparammask.md">RILUICCLOCKSTATEPARAMMASK</a> enumeration values that indicates which members of the structure contain valid data. A member of the structure is valid if the corresponding bit flag is set.

`rilUiccLock`

Specifies the lock of type <a href="..\rilapitypes\ns-rilapitypes-riluicclock.md">RILUICCLOCK</a>.

`dwLockState`

The current state of the lock, a bitmask of <a href="..\rilapitypes\ne-rilapitypes-riluicclockstatelockstate.md">RILUICCLOCKSTATELOCKSTATE</a>.

`dwVerifyAttemptsLeft`

The number of verification attempts that remain before the lock is blocked.

`dwUnblockAttemptsLeft`

The number of unblock attempts that remain before the lock is permanently blocked.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h (include Ntddrilapitypes.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/dn946511">Cellular COM structures</a>