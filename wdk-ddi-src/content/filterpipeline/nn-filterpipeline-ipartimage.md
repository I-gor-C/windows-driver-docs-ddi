---
UID: NN:filterpipeline.IPartImage
title: IPartImage
author: windows-driver-content
description: The IPartImage interface is the abstraction for images in an XPS document.
old-location: print\ipartimage.htm
old-project: print
ms.assetid: 7bb39a5b-7519-47a6-82ca-440942ae2c84
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPartImage, IPartImage interface [Print Devices], IPartImage interface [Print Devices], described, filterpipeline/IPartImage, filterpipeline_faed49d4-60d1-4063-a4aa-c9ec8c56655d.xml, print.ipartimage
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: filterpipeline.h
req.include-header: Filterpipeline.h
req.target-type: Windows
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
-	filterpipeline.h
api_name:
-	IPartImage
product: Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---

# IPartImage interface

The <b>IPartImage</b> interface is the abstraction for images in an XPS document.

## Methods

<p>The <b>IPartImage</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPartImage::GetImageProperties](nf-filterpipeline-ipartimage-getimageproperties.md) | The GetImageProperties method gets an image property that is based on the content type. |
| [IPartImage::SetImageContent](nf-filterpipeline-ipartimage-setimagecontent.md) | The SetImageContent method sets an image property that is based on the content type. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | filterpipeline.h (include Filterpipeline.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff551846">IPartBase</a>