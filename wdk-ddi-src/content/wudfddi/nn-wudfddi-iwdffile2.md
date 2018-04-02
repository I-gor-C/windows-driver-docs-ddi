---
UID: NN:wudfddi.IWDFFile2
title: IWDFFile2
author: windows-driver-content
description: Drivers obtain the IWDFFile2 interface by calling IWDFFile::QueryInterface.
old-location: wdf\iwdffile2.htm
old-project: wdf
ms.assetid: 49a3defc-d86c-4d70-8c1c-a5abbadda013
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IWDFFile2, IWDFFile2 interface, IWDFFile2 interface, described, UMDFFileObjectRef_991af5dd-c654-4afe-9072-0efeb7ab4d57.xml, umdf.iwdffile2, wdf.iwdffile2, wudfddi/IWDFFile2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.9
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
-	IWDFFile2
product:
- Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IWDFFile2 interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

Drivers obtain the <b>IWDFFile2</b> interface by calling <b>IWDFFile::QueryInterface</b>.

## Methods

<p>The <b>IWDFFile2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDFFile2::GetRelatedFileObject](nf-wudfddi-iwdffile2-getrelatedfileobject.md) | The GetRelatedFileObject method retrieves the IWDFFile interface of a related file object, which is a file object that has a technology-specific relationship with another file object. |
| [IWDFFile2::RetrieveCountedFileName](nf-wudfddi-iwdffile2-retrievecountedfilename.md) | The RetrieveCountedFileName method retrieves the full counted file name for a file that is associated with a device. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.9 |
| **Header** | wudfddi.h |