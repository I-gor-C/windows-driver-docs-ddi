---
UID: NF:wdtf.IWDTFTarget2.GetValueBool
title: IWDTFTarget2::GetValueBool method
author: windows-driver-content
description: Returns a boolean value from the target that is associated with a specified attribute.
old-location: dtf\iwdtftarget2_getvaluebool.htm
old-project: dtf
ms.assetid: 53be5e16-7c04-41c3-a808-828982eda440
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: GetValueBool method [Windows Device Testing Framework], GetValueBool method [Windows Device Testing Framework], IWDTFTarget2 interface, GetValueBool,IWDTFTarget2.GetValueBool, IWDTFTarget2, IWDTFTarget2 interface [Windows Device Testing Framework], GetValueBool method, IWDTFTarget2::GetValueBool, Microsoft.WDTF.IWDTFTarget2.GetValueBool, Microsoft::WDTF::IWDTFTarget2::GetValueBool, dtf.iwdtftarget2_getvaluebool, wdtf/IWDTFTarget2::GetValueBool
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wdtf.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows XP Professional
req.target-min-winversvr: Windows Server 2008
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: WDTF.idl
req.max-support: 
req.namespace: Microsoft.WDTF
req.assembly: WDTF.Interop.metadata_dll
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
-	WDTF.Interop.metadata_dll.dll
api_name:
-	IWDTFTarget2.GetValueBool
product: Windows
targetos: Windows
req.typenames: TTraceLevel
req.product: Windows 10 or later.
---


# IWDTFTarget2::GetValueBool method
Returns a boolean value from the target that is associated with a specified attribute.

## Syntax

```
HRESULT GetValueBool(
  BSTR         SDEL,
  VARIANT_BOOL *pValue
);
```

## Parameters

`SDEL`

An SDEL statement that specifies the attribute value to retrieve.

`pValue`

The address of a variable that receives the result of this method.


## Return Value

If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.

## Remarks

You specify the field that the<b> GetValueBool</b> method retrieves 
by using a regular <a href="https://msdn.microsoft.com/84c2a1d6-6bec-4aeb-b858-c29f50d74390">SDEL</a> 
statement. Typically, an SDEL statement can contain comparison operators and value specifiers to 
perform matches. However, you do not need these items for <b>GetValueBool</b> 
to work properly.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows XP Professional Windows Server 2008 |
| **Target Platform** | Desktop |
| **Header** | wdtf.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/hh439367">IWDTFTarget2</a>