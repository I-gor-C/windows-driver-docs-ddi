---
UID: NS:portcls.__unnamed_struct_0cec_5
title: PCEVENT_ITEM
author: windows-driver-content
description: The PCEVENT_ITEM structure is used to describe an event that is supported by a particular filter, pin, or node.
old-location: audio\pcevent_item.htm
old-project: audio
ms.assetid: b91a7582-e146-4ded-a6b7-cb77850bfd2c
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: PPCEVENT_ITEM, portcls/PPCEVENT_ITEM, PCEVENT_ITEM structure [Audio Devices], *PPCEVENT_ITEM, PPCEVENT_ITEM structure pointer [Audio Devices], portcls/PCEVENT_ITEM, PCEVENT_ITEM, audio.pcevent_item, audpc-struct_54e5d50f-6902-47d3-8170-3ee459b8dfb8.xml
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
-	PCEVENT_ITEM
product: Windows
targetos: Windows
req.typenames: PCEVENT_ITEM, *PPCEVENT_ITEM
---

# *PPCEVENT_ITEM structure
The <b>PCEVENT_ITEM</b> structure is used to describe an event that is supported by a particular filter, pin, or node.

## Syntax
````
typedef struct {
  const GUID         *Set;
  ULONG              Id;
  ULONG              Flags;
  PCPFNEVENT_HANDLER Handler;
} PCEVENT_ITEM, *PPCEVENT_ITEM;
````

## Members


## Remarks
The <b>PCEVENT_ITEM</b> structure specifies a particular event item in an automation table. The <a href="..\portcls\ns-portcls-__unnamed_struct_0cec_6.md">PCAUTOMATION_TABLE</a> structure points to an array of <b>PCEVENT_ITEM</b> structures.

In WDM audio, the target for an event request is either a pin instance or a node on a pin. A filter instance cannot be the target of an event request.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | portcls.h (include Portcls.h) |

## See Also

<a href="..\portcls\ns-portcls-_pcevent_request.md">PCEVENT_REQUEST</a>



<a href="..\portcls\ns-portcls-__unnamed_struct_0cec_6.md">PCAUTOMATION_TABLE</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PCEVENT_ITEM structure%20 RELEASE:%20(2/20/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>