---
UID : NS:minitape.RT_PARAMETER_DATA
title : RT_PARAMETER_DATA
author : windows-driver-content
description : The RT_PARAMETER_DATA structure contains the parameter data for the report timestamp command.
old-location : storage\rt_parameter_data.htm
old-project : storage
ms.assetid : EB23D502-87E4-48B1-B1DC-0B215AB361C8
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : RT_PARAMETER_DATA, *PRT_PARAMETER_DATA, RT_PARAMETER_DATA
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : minitape.h
req.include-header : Minitape.h, Storport.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows 10, version 1709 and later versions of Windows.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RT_PARAMETER_DATA
req.alt-loc : scsi.h
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
req.typenames : "*PRT_PARAMETER_DATA, RT_PARAMETER_DATA"
---

# RT_PARAMETER_DATA structure
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]

The <b>RT_PARAMETER_DATA</b> structure contains the parameter data for the report timestamp command.

## Syntax
````
typedef struct _RT_PARAMETER_DATA {
  UCHAR     ParameterDataLength[2];
  UCHAR Origin  :3;
  UCHAR Reserved1  :5;
  UCHAR Reserved2;
  UCHAR Timestamp[6];
  UCHAR Reserved3[2];
} RT_PARAMETER_DATA, *PRT_PARAMETER_DATA;
````

## Members

        
            `Origin`

            Indicates the most recent event that initialized the returned device clock.

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
        
            `Reserved1`

            Reserved for future use.
        
            `Reserved2`

            Reserved for future use.
        
            `Reserved3`

            Reserved for future use.
        
            `Timestamp`

            Contains the current value of a device clock.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | minitape.h (include Minitape.h, Storport.h) |

    ## See Also

        <dl>
<dt>
<a href="..\scsi\ns-scsi-st_parameter_data.md">ST_PARAMETER_DATA</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20RT_PARAMETER_DATA structure%20 RELEASE:%20(1/10/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>