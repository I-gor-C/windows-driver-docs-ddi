---
UID: NC.evntrace.PEVENT_RECORD_CALLBACK
title: PEVENT_RECORD_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 78deb800-4bd1-442d-8b48-dfa9b583a53b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: evntrace.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# PEVENT_RECORD_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PEVENT_RECORD_CALLBACK PeventRecordCallback; 

// Definition

VOID PeventRecordCallback 
(
	PEVENT_RECORD EventRecord
)
{...}

PEVENT_RECORD_CALLBACK 


```

## -parameters

### -param EventRecord: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also