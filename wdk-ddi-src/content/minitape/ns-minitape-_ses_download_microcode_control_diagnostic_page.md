---
UID : NS:minitape._SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE
title : _SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE
author : windows-driver-content
description : The SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure contains a vendor specific microcode (i.e., firmware) image for use by the enclosure services process.
old-location : storage\ses_download_microcode_control_diagnostic_page.htm
old-project : storage
ms.assetid : 09c2746f-cfe4-41dc-82ce-0b7e0c348897
ms.author : windowsdriverdev
ms.date : 1/10/2018
ms.keywords : _SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE, *PSES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE, SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE
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
req.alt-api : SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE
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
req.typenames : "*PSES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE, SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE"
---

# _SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure
The <b>SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE</b> structure contains a vendor specific microcode (i.e., firmware) image
for use by the enclosure services process.

## Syntax
````
typedef struct _SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE {
  UCHAR  PageCode;
  UCHAR  SubEnclosureId;
  UCHAR  PageLength[2];
  UCHAR  ExpectedGenerationCode[4];
  UCHAR  Mode;
  UCHAR  Reserved[2];
  UCHAR  BufferID;
  UCHAR  BufferOffset[4];
  UCHAR  ImageLength[4];
  UCHAR  DataLength[4];
  UCHAR  Data[ANYSIZE_ARRAY];
} SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE, *PSES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE;
````

## Members

        
            `BufferID`

            Specifies a specific buffer within the enclosure services process to receive the microcode
image. The enclosure services process assigns vendor specific buffer ID codes to buffers (e.g., the main
firmware image may be stored in buffer 00h and a backup firmware image may be stored in buffer 01h). The
enclosure services process shall support a buffer ID value of 00h. If more than one buffer is supported, then
the enclosure services process shall assign additional buffer ID codes contiguously, beginning with 01h. If the
enclosure services process receives an unsupported buffer ID code, then it shall abort the download
microcode operation and set the <i>Status</i> field in <a href="https://msdn.microsoft.com/af686e7a-9426-4151-8ac4-d95ae1689b4c">SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR</a>  to 0x80 in the <a href="https://msdn.microsoft.com/4572040b-c234-4281-b9d7-14d7f2bb7506">SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE</a> structure.
        
            `BufferOffset`

            Specifies the offset in bytes within the buffer to which the microcode data is written in multiples of four. The enclosure services process may require that this  field be contiguously increasing in consecutive SEND DIAGNOSTIC commands.
        
            `Data`

            Contains part of the vendor specific microcode image.
        
            `DataLength`

            Specifies the length of <i>Data</i>, in bytes.
        
            `ExpectedGenerationCode`

            Specifies the expected value of the generation code. If this parameter is not set to the current generation code, then the enclosure services
process shall abort the download microcode operation with a status of 0x80.
        
            `ImageLength`

            specifies the total number of bytes in the microcode image the application
intends to send to the specified <i>BufferID</i>.
        
            `Mode`

            Specifies which mode to download the microcode with. 

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `PageCode`

            Specifies the diagnostic page being sent or requested based on the value. For a Microcode Control diagnostic page, the value should be 0x0E.
        
            `PageLength`

            Specifies the number of bytes that follow in the diagnostic page.
        
            `Reserved`

            
        
            `SubEnclosureId`

            Specifies the sub enclosure to which the application client is
sending the microcode image. If the value does not match a valid SUBENCLOSURE_IDENTIFIER field value found in the <a href="..\scsi\ns-scsi-_ses_configuration_diagnostic_page.md">SES_CONFIGURATION_DIAGNOSTIC_PAGE</a>, then the enclosure services
process shall abort the download microcode operation with a status of 0x80.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | minitape.h (include Minitape.h, Storport.h) |