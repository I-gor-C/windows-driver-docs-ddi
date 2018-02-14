---
UID: NS:nfcsedev._SECURE_ELEMENT_EVENT_INFO
title: "_SECURE_ELEMENT_EVENT_INFO"
author: windows-driver-content
description: This structure provides information about a secure element event.
old-location: nfpdrivers\secure_element_event_info.htm
old-project: nfpdrivers
ms.assetid: 72B31C26-89D3-49B2-A404-E6F096D0A334
ms.author: windowsdriverdev
ms.date: 12/18/2017
ms.keywords: nfcsedev/PSECURE_ELEMENT_EVENT_INFO, SECURE_ELEMENT_EVENT_INFO, PSECURE_ELEMENT_EVENT_INFO structure pointer [Near-Field Proximity Drivers], _SECURE_ELEMENT_EVENT_INFO, SECURE_ELEMENT_EVENT_INFO structure [Near-Field Proximity Drivers], nfpdrivers.secure_element_event_info, *PSECURE_ELEMENT_EVENT_INFO, nfcsedev/SECURE_ELEMENT_EVENT_INFO, PSECURE_ELEMENT_EVENT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: nfcsedev.h
req.include-header: 
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
-	nfcsedev.h
apiname:
-	SECURE_ELEMENT_EVENT_INFO
product: Windows
targetos: Windows
req.typenames: SECURE_ELEMENT_EVENT_INFO, *PSECURE_ELEMENT_EVENT_INFO
---

# _SECURE_ELEMENT_EVENT_INFO structure
This structure provides information about a secure element event.

## Syntax
````
typedef struct _SECURE_ELEMENT_EVENT_INFO {
  GUID                                     guidSecureElementId;
  SECURE_ELEMENT_EVENT_TYPE                eEventType;
  DWORD                                    cbEventData;
  _Field_size_bytes_(cbEventData)
    BYTE pbEventData[ANYSIZE_ARRAY];
} SECURE_ELEMENT_EVENT_INFO, *PSECURE_ELEMENT_EVENT_INFO;
````

## Members


`cbEventData`

This is the amount of bytes for the pbEventData array.

`eEventType`

This is an event type. For more information about the types, see the <a href="..\nfcsedev\ne-nfcsedev-_secure_element_event_type.md">SECURE_ELEMENT_EVENT_TYPE</a> enumeration topic.

`guidSecureElementId`

This is a unique identifier for the secure element.

`pbEventData`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | nfcsedev.h |