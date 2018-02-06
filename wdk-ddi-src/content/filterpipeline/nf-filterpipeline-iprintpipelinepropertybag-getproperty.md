---
UID: NF:filterpipeline.IPrintPipelinePropertyBag.GetProperty
title: IPrintPipelinePropertyBag::GetProperty method
author: windows-driver-content
description: The GetProperty method gets a property from a property bag.
old-location: print\iprintpipelinepropertybag_getproperty.htm
old-project: print
ms.assetid: 10a5ada8-98ab-4e1c-a4b5-2f6d60674952
ms.author: windowsdriverdev
ms.date: 2/2/2018
ms.keywords: GetProperty method [Print Devices], IPrintPipelinePropertyBag interface, print.iprintpipelinepropertybag_getproperty, filterpipeline/IPrintPipelinePropertyBag::GetProperty, GetProperty, IPrintPipelinePropertyBag::GetProperty, GetProperty method [Print Devices], IPrintPipelinePropertyBag, filterpipeline_6a2e804b-b8dd-4e20-a71a-7817181b825c.xml, IPrintPipelinePropertyBag interface [Print Devices], GetProperty method
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: filterpipeline.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: Filterpipeline.idl
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: filterpipeline.h
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	filterpipeline.h
apiname:
-	IPrintPipelinePropertyBag.GetProperty
product: Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---


# GetProperty method
The <code>GetProperty</code> method gets a property from a property bag.

## Syntax

````
HRESULT GetProperty(
  [in]  const wchar_t *pszName,
  [out]       VARIANT *pVar
);
````

## Parameters

`pszName`

The name of the property that you want to get from the property bag.

`pVar`

The <b>VARIANT</b> value to get from the property bag.


## Return Value

<code>GetProperty</code> returns an <b>HRESULT</b> value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | filterpipeline.h |
| **Library** | filterpipeline.h |