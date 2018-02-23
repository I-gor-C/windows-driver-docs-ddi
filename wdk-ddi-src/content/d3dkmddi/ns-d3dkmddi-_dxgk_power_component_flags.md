---
UID: NS:d3dkmddi._DXGK_POWER_COMPONENT_FLAGS
title: "_DXGK_POWER_COMPONENT_FLAGS"
author: windows-driver-content
description: Describes state transition information about a power component.
old-location: display\dxgk_power_component_flags.htm
old-project: display
ms.assetid: aa8cce5b-d582-4c5b-99e2-fad1f0e80128
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: d3dkmddi/DXGK_POWER_COMPONENT_FLAGS, DXGK_POWER_COMPONENT_FLAGS structure [Display Devices], _DXGK_POWER_COMPONENT_FLAGS, display.dxgk_power_component_flags, DXGK_POWER_COMPONENT_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
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
req.irql: PASSIVE_LEVEL
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	D3dkmddi.h
apiname:
-	DXGK_POWER_COMPONENT_FLAGS
product: Windows
targetos: Windows
req.typenames: DXGK_POWER_COMPONENT_FLAGS
---

# _DXGK_POWER_COMPONENT_FLAGS structure
Describes state transition information about a power component.

## Syntax
````
typedef struct _DXGK_POWER_COMPONENT_FLAGS {
  union {
    struct {
      UINT Reserved0  :1;
      UINT DriverCompletesFStateTransition  :1;
      UINT TransitionTo_F0_OnDx  :1;
      UINT Reserved  :29;
    };
    UINT Value;
  };
} DXGK_POWER_COMPONENT_FLAGS;
````

## Members



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Header** | d3dkmddi.h (include D3dkmddi.h) |

## See Also

<a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb_completefstatetransition.md">DxgkCbCompleteFStateTransition</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_POWER_COMPONENT_FLAGS structure%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>