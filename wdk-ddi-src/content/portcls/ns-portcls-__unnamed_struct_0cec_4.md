---
UID: NS:portcls.__unnamed_struct_0cec_4
title: "*PPCMETHOD_ITEM"
author: windows-driver-content
description: The PCMETHOD_ITEM structure describes a method supported by a filter, pin, or node.
old-location: audio\pcmethod_item.htm
old-project: audio
ms.assetid: 588d2f0e-0f87-46c7-b2fa-f14f29f6a9f0
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: PPCMETHOD_ITEM structure pointer [Audio Devices], *PPCMETHOD_ITEM, portcls/PCMETHOD_ITEM, PCMETHOD_ITEM, audio.pcmethod_item, PCMETHOD_ITEM structure [Audio Devices], audpc-struct_58edb038-1bae-4846-8ce9-d0c0c052730c.xml, PPCMETHOD_ITEM, portcls/PPCMETHOD_ITEM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: portcls.h
req.include-header: Portcls.h
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
req.irql: PASSIVE_LEVEL
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	portcls.h
apiname:
-	PCMETHOD_ITEM
product: Windows
targetos: Windows
req.typenames: "*PPCMETHOD_ITEM, PCMETHOD_ITEM"
---

# *PPCMETHOD_ITEM structure
The PCMETHOD_ITEM structure describes a method supported by a filter, pin, or node.

## Syntax
````
typedef struct {
  const GUID          *Set;
  ULONG               Id;
  ULONG               Flags;
  PCPFNMETHOD_HANDLER Handler;
} PCMETHOD_ITEM, *PPCMETHOD_ITEM;
````

## Members


## Remarks
The WDM audio subsystem does not currently support methods on either filter instances or pin instances. This restriction also precludes support for methods on nodes.

The <a href="..\portcls\ns-portcls-__unnamed_struct_0cec_6.md">PCAUTOMATION_TABLE</a> structure contains a pointer to an array of PCMETHOD_ITEM structures.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | portcls.h (include Portcls.h) |

## See Also

<a href="..\portcls\ns-portcls-_pcmethod_request.md">PCMETHOD_REQUEST</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PCMETHOD_ITEM structure%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>