---
UID: NC.ucxsstreams.PFN_UCXSTATICSTREAMSSETSTREAMINFO
title: *PFN_UCXSTATICSTREAMSSETSTREAMINFO
author: windows-driver-content
description: 
ms.assetid: b9d19758-f866-4a5f-95e8-c312c4396971
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucxsstreams.h
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

# *PFN_UCXSTATICSTREAMSSETSTREAMINFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UCXSTATICSTREAMSSETSTREAMINFO *PfnUcxstaticstreamssetstreaminfo; 

// Definition

VOID *PfnUcxstaticstreamssetstreaminfo 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	UCXSSTREAMS StaticStreams
	PSTREAM_INFO StreamInfo
)
{...}

*PFN_UCXSTATICSTREAMSSETSTREAMINFO 


```

## -parameters

### -param DriverGlobals: 
### -param StaticStreams: 
### -param StreamInfo: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also