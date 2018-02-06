---
UID: NC:drmk.PFNDRMADDCONTENTHANDLERS
title: PFNDRMADDCONTENTHANDLERS
author: windows-driver-content
description: This callback function is reserved for system use.
old-location: audio\pfndrmaddcontenthandlers.htm
old-project: audio
ms.assetid: 762604FC-34EA-41A1-9F2B-B3852AA4D167
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: audio.pfndrmaddcontenthandlers, DRMAddContentHandlers callback function [Audio Devices], DRMAddContentHandlers, PFNDRMADDCONTENTHANDLERS, PFNDRMADDCONTENTHANDLERS, drmk/DRMAddContentHandlers, DRMAddContentHandlers callback function [Audio Devices], DRMAddContentHandlers
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: drmk.h
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
-	UserDefined
apilocation:
-	Drmk.h
apiname:
-	DRMAddContentHandlers
product: Windows
targetos: Windows
req.typenames: "*PWDI_TX_METADATA, WDI_TX_METADATA"
---


# PFNDRMADDCONTENTHANDLERS callback function
This callback function is reserved for system use.

## Syntax

```
PFNDRMADDCONTENTHANDLERS Pfndrmaddcontenthandlers;

NTSTATUS Pfndrmaddcontenthandlers(
  ULONG ContentId,
  PVOID *paHandlers,
  ULONG NumHandlers
)
{...}
```

## Parameters

`ContentId`

This parameter is reserved for system use.

`*paHandlers`

This parameter is reserved for system use.

`NumHandlers`

This parameter is reserved for system use.


## Return Value

This return value is reserved for system use.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | drmk.h |