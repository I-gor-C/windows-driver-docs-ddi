---
UID: NN:wudfddi.IWDFFile
title: IWDFFile
author: windows-driver-content
description: The IWDFFile interface exposes the file object that represents the HANDLE that is returned by the Microsoft Win32 CreateFile function.
old-location: wdf\iwdffile.htm
old-project: wdf
ms.assetid: bf8e5ab1-9a17-4eb5-8c54-34670ea27068
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IWDFFile, IWDFFile interface, IWDFFile interface, described, UMDFFileObjectRef_41506c7e-3abb-4f41-ab23-a69114c3fdbd.xml, umdf.iwdffile, wdf.iwdffile, wudfddi/IWDFFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	WUDFx.dll
api_name:
-	IWDFFile
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IWDFFile interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <a href="https://msdn.microsoft.com/library/windows/hardware/ff558912">IWDFFile</a> interface exposes the file object that represents the HANDLE that is returned by the Microsoft Win32 <b>CreateFile</b> function. All further operations on this handle, such as calls to the Win32 <b>ReadFile</b> function and the <b>DeviceIoControl</b> function, are sent to this file object.

## Methods

<p>The <b>IWDFFile</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDFFile::GetDevice](nf-wudfddi-iwdffile-getdevice.md) | The GetDevice method returns the interface to the device object that a file object is associated with. |
| [IWDFFile::RetrieveFileName](nf-wudfddi-iwdffile-retrievefilename.md) | The RetrieveFileName method retrieves the full name of the file that is associated with the underlying kernel-mode device. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfddi.h |