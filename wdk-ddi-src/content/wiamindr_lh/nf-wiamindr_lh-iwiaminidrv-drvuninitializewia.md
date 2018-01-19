---
UID : NF:wiamindr_lh.IWiaMiniDrv.drvUnInitializeWia
title : IWiaMiniDrv::drvUnInitializeWia method
author : windows-driver-content
description : The IWiaMiniDrv::drvUnInitializeWia method releases resources held by the minidriver.
old-location : image\iwiaminidrv_drvuninitializewia.htm
old-project : image
ms.assetid : 974de3b5-c129-42ee-a522-071c26726cf1
ms.author : windowsdriverdev
ms.date : 1/17/2018
ms.keywords : IWiaMiniDrv, IWiaMiniDrv::drvUnInitializeWia, drvUnInitializeWia
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : wiamindr_lh.h
req.include-header : Wiamindr.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows Me and in Windows XP and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IWiaMiniDrv.drvUnInitializeWia
req.alt-loc : wiamindr_lh.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PSCANWINDOW, SCANWINDOW"
req.product : Windows 10 or later.
---


# drvUnInitializeWia method
The <b>IWiaMiniDrv::drvUnInitializeWia</b> method releases resources held by the minidriver.

## Syntax

````
HRESULT drvUnInitializeWia(
  [in] BYTE *pWiasContext
);
````

## Parameters

`__MIDL__IWiaMiniDrv0064`




## Return Value

On success, the method should return S_OK If the method fails, it should return a standard COM error code.

## Remarks

The WIA service calls the <b>IWiaMiniDrv::drvUnInitializeWia</b> method when the resources associated with an application item tree are no longer needed. The minidriver can then unload any DLLs and free any allocated memory.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wiamindr_lh.h (include Wiamindr.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\wiamindr_lh\nn-wiamindr_lh-iwiaminidrv.md">IWiaMiniDrv</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544986">IWiaMiniDrv::drvInitializeWia</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20IWiaMiniDrv::drvUnInitializeWia method%20 RELEASE:%20(1/17/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>