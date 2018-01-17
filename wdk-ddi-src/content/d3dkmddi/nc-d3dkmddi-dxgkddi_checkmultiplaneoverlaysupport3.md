---
UID: NC:d3dkmddi.DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3
title: DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3 function
author: windows-driver-content
description: The following new function is called to determine whether a specific multi-plane overlay configuration is supported.
old-location: display\dxgkddi_checkmultiplaneoverlaysupport3.htm
old-project: display
ms.assetid: 2EA7E8C4-51E0-4BDE-B69B-1A40FEB82952
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3
req.alt-loc: d3dkmddi.h
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
req.typenames: D3D12DDI_WRITEBUFFERIMMEDIATE_PARAMETER_0032
---

# DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3 function



## -description
The following new function is called to determine whether a specific multi-plane overlay configuration is supported. 



## -syntax

````
NTSTATUS APIENTRY DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3(
  _In_    const HANDLE                                   hAdapter,
  _Inout_       PDXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT3  pCheckSupport
);
````


## -parameters

### -param hAdapter [in]

Identifies the adapter containing the overlay hardware.


### -param pCheckSupport [in, out]

A pointer to a DXGKARG_CHECKMULTIPLANEOVERLAYSUPPORT3 structure that describes the surfaces and display options to present.


## -returns
DXGKDDI_CHECKMULTIPLANEOVERLAYSUPPORT3 returns the following values:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>If the routine has been successfully completed.

 


## -remarks
The kernel mode driver reports whether the specified configuration is supported.  The kernel mode driver should not raise or lower the available bandwidth in anticipation to this configuration getting set.

This function is always called at PASSIVE level.
</p>