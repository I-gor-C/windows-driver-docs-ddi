---
UID: NS:windot11._DOT11_WFD_INVITATION_FLAGS
title: "_DOT11_WFD_INVITATION_FLAGS"
author: windows-driver-content
description: The DOT11_WFD_INVITATION_FLAGS structure represents the Invitation Attributes used during the Invitation procedure.
old-location: netvista\dot11_wfd_invitation_flags.htm
old-project: netvista
ms.assetid: 9743FF37-0E8A-499F-AADB-9CD7BDC381E0
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: Join, _DOT11_WFD_INVITATION_FLAGS, DOT11_WFD_INVITATION_FLAGS, *PDOT11_WFD_INVITATION_FLAGS, DOT11_WFD_INVITATION_FLAGS structure [Network Drivers Starting with Windows Vista], PDOT11_WFD_INVITATION_FLAGS, windot11/PDOT11_WFD_INVITATION_FLAGS, netvista.dot11_wfd_invitation_flags, Reinvoke, windot11/DOT11_WFD_INVITATION_FLAGS, PDOT11_WFD_INVITATION_FLAGS structure pointer [Network Drivers Starting with Windows Vista]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: windot11.h
req.include-header: Windot11.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with   Windows 8.
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
-	Windot11.h
apiname:
-	DOT11_WFD_INVITATION_FLAGS
product: Windows
targetos: Windows
req.typenames: DOT11_WFD_INVITATION_FLAGS, *PDOT11_WFD_INVITATION_FLAGS
req.product: Windows 10 or later.
---

# _DOT11_WFD_INVITATION_FLAGS structure
<div class="alert"><b>Important</b>  The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560689">Native 802.11 Wireless LAN</a> interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see <a href="https://msdn.microsoft.com/6EF92E34-7BC9-465E-B05D-2BCB29165A18">WLAN Universal Windows driver model</a>.</div><div> </div>The <b>DOT11_WFD_INVITATION_FLAGS</b> structure represents the Invitation Attributes used during the Invitation procedure.

## Syntax
````
typedef struct _DOT11_WFD_INVITATION_FLAGS {
  UCHAR InvitationType:1;
  UCHAR Reserved:7;
} DOT11_WFD_INVITATION_FLAGS, *PDOT11_WFD_INVITATION_FLAGS;
````

## Members


`InvitationType`



`Reserved`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported starting with   Windows 8. Supported starting with   Windows 8. |
| **Header** | windot11.h (include Windot11.h) |