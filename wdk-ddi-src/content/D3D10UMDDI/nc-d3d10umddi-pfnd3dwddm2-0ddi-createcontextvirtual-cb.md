---
UID: NC.d3d10umddi.PFND3DWDDM2_0DDI_CREATECONTEXTVIRTUAL_CB
title: PFND3DWDDM2_0DDI_CREATECONTEXTVIRTUAL_CB
author: windows-driver-content
description: 
ms.assetid: dae58705-860f-4bbd-b86d-49de23d0e3df
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3d10umddi.h
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

# PFND3DWDDM2_0DDI_CREATECONTEXTVIRTUAL_CB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DWDDM2_0DDI_CREATECONTEXTVIRTUAL_CB Pfnd3dwddm20DdiCreatecontextvirtualCb; 

// Definition

HRESULT Pfnd3dwddm20DdiCreatecontextvirtualCb 
(
	D3D10DDI_HRTCORELAYER hDevice
	D3DWDDM2_0DDICB_CREATECONTEXTVIRTUAL *
)
{...}

PFND3DWDDM2_0DDI_CREATECONTEXTVIRTUAL_CB 


```

## -parameters

### -param hDevice: 
### -param *: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also