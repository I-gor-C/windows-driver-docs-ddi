---
UID: NF:prcomoem.IPrintCoreHelper.EnumOptions
title: IPrintCoreHelper::EnumOptions method
author: windows-driver-content
description: The IPrintCoreHelper::EnumOptions method gets a list of available options for the given feature.
old-location: print\iprintcorehelper_enumoptions.htm
old-project: print
ms.assetid: 2e46e8cd-b5e5-4116-b42c-b7adcee9d520
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: EnumOptions method [Print Devices], EnumOptions method [Print Devices], IPrintCoreHelper interface, EnumOptions,IPrintCoreHelper.EnumOptions, IPrintCoreHelper, IPrintCoreHelper interface [Print Devices], EnumOptions method, IPrintCoreHelper::EnumOptions, prcomoem/IPrintCoreHelper::EnumOptions, print.iprintcorehelper_enumoptions, print_unidrv-pscript_allplugins_2dc1f4f3-27ab-44d3-8778-45f2eafae92a.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	Prcomoem.h
api_name:
-	IPrintCoreHelper.EnumOptions
product: Windows
targetos: Windows
req.typenames: OEMPTOPTS, *POEMPTOPTS
req.product: Windows 10 or later.
---


# IPrintCoreHelper::EnumOptions method
The <b>IPrintCoreHelper::EnumOptions</b> method gets a list of available options for the given feature.

## Syntax

```
HRESULT EnumOptions(
  PCSTR      pszFeatureKeyword,
  PCSTR * [] pOptionList,
  DWORD      *pdwNumOptions
);
```

## Parameters

`pszFeatureKeyword`

An ANSI character string that contains the feature whose options are requested.

`pOptionList`



`pdwNumOptions`

A pointer to a variable that receives the number of options in the option array that is pointed to by the <i>pOptionList</i> parameter.


## Return Value

<b>IPrintCoreHelper::EnumOptions</b> should return S_OK if the operation succeeds. Otherwise, this method should return a standard COM error code.

## Remarks

When <b>IPrintCoreHelper::EnumOptions</b> returns, the option list contains all options, regardless of constraints or other factors.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | prcomoem.h (include Prcomoem.h) |

## See Also

<a href="https://msdn.microsoft.com/db13410f-e4cb-4077-bb4b-7963e97b435c">IPrintCoreHelper</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552954">IPrintCoreHelper::EnumFeatures</a>