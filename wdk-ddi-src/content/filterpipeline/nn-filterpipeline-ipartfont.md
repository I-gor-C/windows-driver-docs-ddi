---
UID: NN:filterpipeline.IPartFont
title: IPartFont
author: windows-driver-content
description: The IPartFont interface is the abstraction for fonts in a part.
old-location: print\ipartfont.htm
old-project: print
ms.assetid: bdb1ad56-de4c-4a9b-96b6-f9faff4abf65
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPartFont, IPartFont interface [Print Devices], IPartFont interface [Print Devices], described, filterpipeline/IPartFont, filterpipeline_def05492-ca27-43bb-9ec4-273aa432536b.xml, print.ipartfont
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
-	IPartFont
product:
- Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---

# IPartFont interface

The <b>IPartFont</b> interface is the abstraction for fonts in a part.

## Methods

<p>The <b>IPartFont</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPartFont::GetFontProperties](nf-filterpipeline-ipartfont-getfontproperties.md) | The GetFontProperties method gets the font properties. |
| [IPartFont::SetFontContent](nf-filterpipeline-ipartfont-setfontcontent.md) | The SetFontContent method sets the content of the font. |
| [IPartFont::SetFontOptions](nf-filterpipeline-ipartfont-setfontoptions.md) | The SetFontOptions method sets the options for the font. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | filterpipeline.h (include Filterpipeline.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff551846">IPartBase</a>