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
req.lib: prcomoem.h
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


# EnumOptions method
The <b>IPrintCoreHelper::EnumOptions</b> method gets a list of available options for the given feature.

## Syntax

````
STDMETHOD EnumOptions(
  [in]  PCSTR pszFeatureKeyword,
  [out] PCSTR *pOptionList[],
  [out] DWORD *pdwNumOptions
);
````

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
| **Library** | prcomoem.h |

## See Also

<a href="..\prcomoem\nn-prcomoem-iprintcorehelper.md">IPrintCoreHelper</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552954">IPrintCoreHelper::EnumFeatures</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintCoreHelper::EnumOptions method%20 RELEASE:%20(2/26/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>