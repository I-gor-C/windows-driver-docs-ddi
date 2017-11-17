---
UID: NS.ntifs._SECURITY_FUNCTION_TABLE_W
title: SECURITY_FUNCTION_TABLE_W
author: windows-driver-content
description: 
ms.assetid: 75c1f307-a940-4754-b4e1-bd335e00dcd8
ms.author: windowsdriverdev
ms.date: 
ms.topic: struct
ms.prod: windows-hardware
ms.technology: windows-devices
ms.keywords: SECURITY_FUNCTION_TABLE_W, SecurityFunctionTableW, *PSecurityFunctionTableW
req.header: ntifs.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# SECURITY_FUNCTION_TABLE_W structure

## -description



## -struct-fields

### -field unsigned long dwVersion			
 	
### -field ENUMERATE_SECURITY_PACKAGES_FN_W EnumerateSecurityPackagesW			
 	
### -field QUERY_CREDENTIALS_ATTRIBUTES_FN_W QueryCredentialsAttributesW			
 	
### -field ACQUIRE_CREDENTIALS_HANDLE_FN_W AcquireCredentialsHandleW			
 	
### -field FREE_CREDENTIALS_HANDLE_FN FreeCredentialsHandle			
 	
### -field void * Reserved2			
 	
### -field INITIALIZE_SECURITY_CONTEXT_FN_W InitializeSecurityContextW			
 	
### -field ACCEPT_SECURITY_CONTEXT_FN AcceptSecurityContext			
 	
### -field COMPLETE_AUTH_TOKEN_FN CompleteAuthToken			
 	
### -field DELETE_SECURITY_CONTEXT_FN DeleteSecurityContext			
 	
### -field APPLY_CONTROL_TOKEN_FN ApplyControlToken			
 	
### -field QUERY_CONTEXT_ATTRIBUTES_FN_W QueryContextAttributesW			
 	
### -field IMPERSONATE_SECURITY_CONTEXT_FN ImpersonateSecurityContext			
 	
### -field REVERT_SECURITY_CONTEXT_FN RevertSecurityContext			
 	
### -field MAKE_SIGNATURE_FN MakeSignature			
 	
### -field VERIFY_SIGNATURE_FN VerifySignature			
 	
### -field FREE_CONTEXT_BUFFER_FN FreeContextBuffer			
 	
### -field QUERY_SECURITY_PACKAGE_INFO_FN_W QuerySecurityPackageInfoW			
 	
### -field void * Reserved3			
 	
### -field void * Reserved4			
 	
### -field EXPORT_SECURITY_CONTEXT_FN ExportSecurityContext			
 	
### -field IMPORT_SECURITY_CONTEXT_FN_W ImportSecurityContextW			
 	
### -field ADD_CREDENTIALS_FN_W AddCredentialsW			
 	
### -field void * Reserved8			
 	
### -field QUERY_SECURITY_CONTEXT_TOKEN_FN QuerySecurityContextToken			
 	
### -field ENCRYPT_MESSAGE_FN EncryptMessage			
 	
### -field DECRYPT_MESSAGE_FN DecryptMessage			
 	
### -field SET_CONTEXT_ATTRIBUTES_FN_W SetContextAttributesW			
 	
### -field SET_CREDENTIALS_ATTRIBUTES_FN_W SetCredentialsAttributesW			
 	
### -field CHANGE_PASSWORD_FN_W ChangeAccountPasswordW			
 	
### -field void * Reserved9			
 	
### -field QUERY_CONTEXT_ATTRIBUTES_EX_FN_W QueryContextAttributesExW			
 	
### -field QUERY_CREDENTIALS_ATTRIBUTES_EX_FN_W QueryCredentialsAttributesExW			
 	
## -remarks

## -see-also