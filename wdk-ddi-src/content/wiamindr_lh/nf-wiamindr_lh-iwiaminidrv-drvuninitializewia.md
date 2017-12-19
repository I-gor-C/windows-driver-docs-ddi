---
UID: NF.wiamindr_lh.IWiaMiniDrv.drvUnInitializeWia
title: IWiaMiniDrv::drvUnInitializeWia method
author: windows-driver-content
description: The IWiaMiniDrv::drvUnInitializeWia method releases resources held by the minidriver.
old-location: image\iwiaminidrv_drvuninitializewia.htm
old-project: Image
ms.assetid: 974de3b5-c129-42ee-a522-071c26726cf1
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IWiaMiniDrv, IWiaMiniDrv::drvUnInitializeWia, drvUnInitializeWia
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wiamindr_lh.h
req.include-header: Wiamindr.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Me and in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IWiaMiniDrv.drvUnInitializeWia
req.alt-loc: wiamindr_lh.h
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
req.product: Windows 10 or later.
---

# IWiaMiniDrv::drvUnInitializeWia method



## -description
The <b>IWiaMiniDrv::drvUnInitializeWia</b> method releases resources held by the minidriver.



## -syntax

````
HRESULT drvUnInitializeWia(
  [in] BYTE *pWiasContext
);
````


## -parameters

### -param pWiasContext [in]

Pointer to a WIA item context.


## -returns
On success, the method should return S_OK If the method fails, it should return a standard COM error code.


## -remarks
The WIA service calls the <b>IWiaMiniDrv::drvUnInitializeWia</b> method when the resources associated with an application item tree are no longer needed. The minidriver can then unload any DLLs and free any allocated memory.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows Me and in Windows XP and later.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wiamindr_lh.h (include Wiamindr.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="image.iwiaminidrv_drvinitializewia">IWiaMiniDrv::drvInitializeWia</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Image\image]:%20IWiaMiniDrv::drvUnInitializeWia method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

